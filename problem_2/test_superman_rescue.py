import unittest
from superman_rescue import (
    get_maximum_number_of_chicken_protected_by_superman,
)


class TestBabyBoss(unittest.TestCase):

    ASSERT_FAIL_GET_WRONG_VALUE_TEXT = (
        "wrong response from the get_number_of_chicken_protected_by_superman function"
    )

    def test_get_maximum_1(self):
        self.assertEqual(
            get_maximum_number_of_chicken_protected_by_superman(
                5, 5, [2, 5, 10, 12, 15]
            ),
            2,
            self.ASSERT_FAIL_GET_WRONG_VALUE_TEXT,
        )

    def test_get_maximum_2(self):
        self.assertEqual(
            get_maximum_number_of_chicken_protected_by_superman(
                6, 10, [1, 11, 30, 34, 35, 37]
            ),
            4,
            self.ASSERT_FAIL_GET_WRONG_VALUE_TEXT,
        )

    def test_get_maximum_edge_case_minN_minK(self):
        self.assertEqual(
            get_maximum_number_of_chicken_protected_by_superman(1, 1, [1]),
            1,
            self.ASSERT_FAIL_GET_WRONG_VALUE_TEXT,
        )

    def test_get_maximum_edge_case_minN_maxK(self):
        self.assertEqual(
            get_maximum_number_of_chicken_protected_by_superman(1, 1000000, [1]),
            1,
            self.ASSERT_FAIL_GET_WRONG_VALUE_TEXT,
        )

    def test_get_maximum_edge_case_maxN_minK(self):
        self.assertEqual(
            get_maximum_number_of_chicken_protected_by_superman(
                1000000, 1, [i for i in range(0, 1000000)]
            ),
            1,
            self.ASSERT_FAIL_GET_WRONG_VALUE_TEXT,
        )

    def test_get_maximum_edge_case_maxN_maxK(self):
        self.assertEqual(
            get_maximum_number_of_chicken_protected_by_superman(
                1000000, 1000000, [i for i in range(0, 1000000)]
            ),
            1000000,
            self.ASSERT_FAIL_GET_WRONG_VALUE_TEXT,
        )
