import unittest
import requests


class TestCaseApp(unittest.TestCase):
    def test_create_task(self):
        response = requests.post("http://127.0.0.1:5000/tasks", json={"title": "TestCase"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "TestCase")

    def test_get_task_without_id(self):  # проверка способа get без учёта id
        response = requests.get("http://127.0.0.1:5000/tasks")
        self.assertEqual(response.status_code, 200)
        data = response.json()

    def test_get_task(self):  # проверка получение задачи с определенным айди
        response = requests.get("http://127.0.0.1:5000/tasks/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)

    def test_put_task(self):
        response = requests.put("http://127.0.0.1:5000/tasks/1", json={"title": "testcase_put"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "testcase_put")


if __name__ == "__main__":
    unittest.main()
