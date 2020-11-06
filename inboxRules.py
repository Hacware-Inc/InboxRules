
from pyews import UserConfiguration, GetInboxRules


userconfig = UserConfiguration('user_email','user_password')

inboxRules = GetInboxRules('user_email', userconfig).response

for i in inboxRules:
      for j in i:
            print(j, ":",i[j])
