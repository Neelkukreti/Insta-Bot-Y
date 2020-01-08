# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'food_reviewers_guide'
insta_password = 'ilovegoogle'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

session.set_do_follow(enabled=False, percentage=100)
session.set_comments(["Cool", "Super!"])
session.set_do_comment(enabled=True, percentage=100)
session.set_do_like(True, percentage=70)
session.interact_by_users(['kneelbefore_me'], amount=1, randomize=True, media='Photo')