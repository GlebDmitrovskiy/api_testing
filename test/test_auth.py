from typing import assert_type

from config.base_test import BaseTest
import pytest


class TestAuth(BaseTest):
    def test_positive_create_token(self):
        response = self.api_auth.create_token(username="admin", password="password123")
        assert response.status_code == 200, response.json()
        assert 'token' in response.json()


    def test_negative_create_token(self):
        response = self.api_auth.create_token(username="admin", password="gavno")
        assert response.status_code == 200, response.json()
        assert 'reason' in response.json()