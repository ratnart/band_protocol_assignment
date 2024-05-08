import unittest
from baby_boss import identify_baby_boss_habit


class TestBabyBoss(unittest.TestCase):

    GOOD_BOY_TEXT = "Good boy"
    BAD_BOY_TEXT = "Bad boy"

    ASSERT_FAIL_MISIDENTIFY_TEXT = "misidentify boss baby's habit"

    def test_identify_baby_boss_habit_1(self):
        self.assertEqual(
            identify_baby_boss_habit("SRSSRRR"),
            self.GOOD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_2(self):
        self.assertEqual(
            identify_baby_boss_habit("RSSRR"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_3(self):
        self.assertEqual(
            identify_baby_boss_habit("SSSRRRRS"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_4(self):
        self.assertEqual(
            identify_baby_boss_habit("SRRSSR"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_5(self):
        self.assertEqual(
            identify_baby_boss_habit("SSRSRRR"),
            self.GOOD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_edge_case_max_length_with_S(self):
        input_string = "S" * 1000000
        self.assertEqual(
            identify_baby_boss_habit(input_string),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_edge_case_max_length_with_R(self):
        input_string = "R" * 1000000
        self.assertEqual(
            identify_baby_boss_habit(input_string),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_edge_case_max_length_with_SR_order(self):
        input_string = "SR" * 500000
        self.assertEqual(
            identify_baby_boss_habit(input_string),
            self.GOOD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_edge_case_one_S(self):
        self.assertEqual(
            identify_baby_boss_habit("S"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )

    def test_identify_baby_boss_habit_edge_case_one_R(self):
        self.assertEqual(
            identify_baby_boss_habit("R"),
            self.BAD_BOY_TEXT,
            self.ASSERT_FAIL_MISIDENTIFY_TEXT,
        )
