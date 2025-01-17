# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'food_reviewers_guide'
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5090,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["", ""])

    # activities

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)...
    """
    session.follow_user_followers(['jiit_lol_b', 'jiit_bakchod', 'laughwithshivansh'], amount=500,
                                  randomize=False, interact=False)

    """ First step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Second step of Massive Follow...
    """
    session.follow_user_followers(['jiit_lol', 'jiit_bakchod', 'laughwithshivansh'], amount=500,
                                  randomize=False, interact=False)

    """ Second step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Clean all followed user - Unfollow all users followed by InstaPy...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=601)

    """ Joining Engagement Pods...
    """
    photo_comments = ['Nice shot! @{}',
        'Awesome! @{}',
        'Cool :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Nice @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

    session.set_do_comment(enabled = False, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods(topic='', engagement_mode='no_comments')
