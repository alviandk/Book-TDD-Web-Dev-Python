#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from book_tester import ChapterTest

class Chapter12Test(ChapterTest):
    chapter_no = 12

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing with git ref')
        self.assertEqual(self.listings[1].type, 'test')
        self.assertEqual(self.listings[2].type, 'output')

        # prep
        self.sourcetree.start_with_checkout(self.chapter_no)
        self.prep_database()

        # skips
        self.skip_with_check(37, '# should show changes') # diff

        # hack fast-forward
        skip = False
        if skip:
            self.pos = 64
            self.sourcetree.run_command('git checkout {0}'.format(
                self.sourcetree.get_commit_spec('ch12l054')
            ))


        while self.pos < len(self.listings):
            print(self.pos, self.listings[self.pos].type)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(self.chapter_no)


if __name__ == '__main__':
    unittest.main()
