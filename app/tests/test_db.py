# -*- coding: utf-8 -*-

"""
Tests for db
"""

import unittest
import app.db.question as dbquestion


class QuestionTestCase(unittest.TestCase):

        
    def test_store_questions(self):
        dbquestion.store(question_id = 1, service = 'fooservice', title = 'footitle', tags = ['tag1', 'tag2'])
        questions_list = dbquestion.get_top_printed()
        self.assertEquals(len(questions_list), 1)
        self.assertEquals(questions_list[0].question_id, 1)
        dbquestion.store(question_id = 1, service = 'fooservice', title = 'footitle', tags = ['tag1', 'tag2'])
        self.assertEquals(len(questions_list), 1)
        self.assertEquals(questions_list[0].question_id, 1)
        dbquestion.store(question_id = 2, service = 'fooservice', title = 'footitle2', tags = ['tag1', 'tag2'])
        questions_list = dbquestion.get_top_printed()
        self.assertEquals(len(questions_list), 2)
        self.assertEquals(questions_list[0].question_id, 1)
        self.assertEquals(questions_list[1].question_id, 2)
        dbquestion.store(question_id = 2, service = 'fooservice', title = 'footitle2', tags = ['tag1', 'tag2'])
        dbquestion.store(question_id = 2, service = 'fooservice', title = 'footitle2', tags = ['tag1', 'tag2'])
        questions_list = dbquestion.get_top_printed()
        self.assertEquals(len(questions_list), 2)
        self.assertEquals(questions_list[0].question_id, 2)
        self.assertEquals(questions_list[1].question_id, 1)
        self.assertEquals(questions_list[1].tags, ['tag1', 'tag2'])
        
if __name__ == '__main__':
    unittest.main()
