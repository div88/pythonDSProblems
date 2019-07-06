# Active Directory
# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
# We can construct this hierarchy as such. 
# Where User is represented by str representing their ids.
import gc

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_user("child_user1")
child.add_user("child_user2")


child.add_group(sub_child)
parent.add_group(child)


# Write a function that provides an efficient look up of whether the user 
# is in a group.

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    g = group.get_users()
    
    if user in g:
        print(f'{user} is in True')
        return True
    else:
        gs = group.get_groups();
        for i in gs:
            is_user_in_group(user,i)
    print(f'{user} is in False')
    return False
        

    return None



is_user_in_group("child_user1",child)
is_user_in_group("child_user2",child)
is_user_in_group("child_user1",parent)
is_user_in_group("sub_child_user",sub_child)
is_user_in_group("sub_child_user10",parent)


