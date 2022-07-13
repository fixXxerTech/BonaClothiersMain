from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = six.text_type(user.pk)
        time = six.text_type(timestamp)
        is_active = six.text_type(user.is_active)
      
        return f"{user_id}{time}{is_active}"

        # return (
        	
        #     six.text_type(user.pk) + six.text_type(timestamp) +
        #     six.text_type(user.is_active)
        # )

account_activation_token = AccountActivationTokenGenerator()
