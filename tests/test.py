import unittest
import requests

# Проводим основные тесты над проектом
class TestCaseApp(unittest.TestCase):
    def test_create_task(self):  # Проверка создание задачи
        response = requests.post("http://127.0.0.1:5000/tasks", json={"title": "TestCase"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "TestCase")
        task_id = data["id"]
        requests.delete(f"http://127.0.0.1:5000/tasks/{task_id}")

    def test_get_task_without_id(self):  # проверка способа get без учёта id
        response = requests.get("http://127.0.0.1:5000/tasks")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data) >= 0, True)

    def test_get_task(self):  # проверка получение задачи с определенным айди
        # Создаем задачу
        response = requests.post("http://127.0.0.1:5000/tasks", json={"title": "Test Task"})
        task_id = response.json()["id"]

        # Получаем задачу по ID
        response = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "Test Task")
        requests.delete(f"http://127.0.0.1:5000/tasks/{task_id}")

    def test_put_task(self):  # Проверка изменения значений в задаче
        # Создаем задачу
        response = requests.post("http://127.0.0.1:5000/tasks", json={"title": "Test Task"})
        task_id = response.json()["id"]

        # Изменяем задачу
        response = requests.put(f"http://127.0.0.1:5000/tasks/{task_id}", json={"title": "Updated Task"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "Updated Task")
        requests.delete(f"http://127.0.0.1:5000/tasks/{task_id}")

    def test_delete_task(self):  # Проверка удаления задачи
        # Создаем задачу
        response = requests.post("http://127.0.0.1:5000/tasks", json={"title": "Test Task"})
        task_id = response.json()["id"]

        # Удаляем задачу
        response = requests.delete(f"http://127.0.0.1:5000/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data, "Задача успешно удалена")


if __name__ == "__main__":
    unittest.main()
