import unittest
import NotesApplication
class NotesApplicationTest (unittest.TestCase):
    """
Testing NotesApplication
    """
    def test_create_empty_notes(self,note_content):
        self.assertEqual(NotesApplication.NotesApplication.create(''), 'enter some notes')
