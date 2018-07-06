class ApiErrors(Exception):

    def empty_result(self, message):
        return "Nothing was found for your keyword " + message

    def responseError(self, error_number):

        if(error_number == 400):
            return 'Something went wrong! Check your params and key and try again!'

        if(error_number == 403):
            return 'OH NO! You try go to private life!!! Sorry we can not allow you do this!'

        if(error_number == 404):
            return 'Houston, we have a problem!!! Nothing was found on this planet by your request! Let\'s go home!'
