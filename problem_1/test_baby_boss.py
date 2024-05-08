import unittest
from baby_boss import (
    identify_baby_boss_habit,
    ERROR_WRONG_INPUT_LENGTH_TEXT,
    ERROR_WRONG_INPUT_TYPE,
)


class TestBabyBoss(unittest.TestCase):

    GOOD_BOY_TEXT = "Good boy"
    BAD_BOY_TEXT = "Bad boy"

    ASSERT_FAIL_MISIDENTIFY_TEXT = "misidentify boss baby's habit"
    ASSERT_FAIL_WRONG_INPUT_LENGTH_TEXT = "String length validation function error"
    ASSERT_FAIL_WRONG_INPUT_TYPE = "Input type validation function error"

    def test_baby_boss_1(self):
        self.assertEqual(
            identify_baby_boss_habit("SRSSRRR"),
            self.GOOD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_baby_boss_2(self):
        self.assertEqual(
            identify_baby_boss_habit("RSSRR"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_baby_boss_3(self):
        self.assertEqual(
            identify_baby_boss_habit("SSSRRRRS"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_baby_boss_4(self):
        self.assertEqual(
            identify_baby_boss_habit("SRRSSR"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_baby_boss_5(self):
        self.assertEqual(
            identify_baby_boss_habit("SSRSRRR"),
            self.GOOD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_baby_boss_edge_case_max_length_with_S(self):
        input_string = "S" * 1000000
        self.assertEqual(
            identify_baby_boss_habit(input_string),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_baby_boss_edge_case_max_length_with_R_order(self):
        input_string = "R" * 1000000
        self.assertEqual(
            identify_baby_boss_habit(input_string),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_baby_boss_edge_case_max_length_with_SR_order(self):
        input_string = "SR" * 500000
        self.assertEqual(
            identify_baby_boss_habit(input_string),
            self.GOOD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_wrong_input_type(self):
        with self.assertRaises(Exception) as context:
            identify_baby_boss_habit(1)
        self.assertTrue(
            ERROR_WRONG_INPUT_TYPE in str(context.exception),
            self.ASSERT_FAIL_WRONG_INPUT_TYPE,
        )

    def test_wrong_input_length_less_than_1(self):
        with self.assertRaises(Exception) as context:
            identify_baby_boss_habit("")
        self.assertTrue(
            ERROR_WRONG_INPUT_LENGTH_TEXT in str(context.exception),
            self.ASSERT_FAIL_WRONG_INPUT_LENGTH_TEXT,
        )

    def test_wrong_input_length_more_than_constraint(self):
        with self.assertRaises(Exception) as context:
            identify_baby_boss_habit("S" * 1000001)
        self.assertTrue(
            ERROR_WRONG_INPUT_LENGTH_TEXT in str(context.exception),
            self.ASSERT_FAIL_WRONG_INPUT_LENGTH_TEXT,
        )
