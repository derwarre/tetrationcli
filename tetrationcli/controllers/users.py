from cement import Controller, ex
import json

class Users(Controller):

    class Meta:
        label = 'users'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(help='list users')
    def users(self):
        restclient = self.app.tetpyclient
        response = restclient.get('/users')
        self.app.log.debug('command returned: %s' % response.status_code)
        data = {}
        data['results'] = json.loads(response.content.decode("utf-8"))
        self.app.log.debug('data returned: %s' % data)
        self.app.render(data, 'users_list.jinja2')