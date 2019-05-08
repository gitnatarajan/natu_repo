from boto.connection import AWSAuthConnection

class ESConnection(AWSAuthConnection):

    def __init__(self, region, **kwargs):
        super(ESConnection, self).__init__(**kwargs)
        self._set_auth_region_name(region)
        self._set_auth_service_name("es")

    def _required_auth_capability(self):
        return ['hmac-v4']

if __name__ == "__main__":

    client = ESConnection(
        region='us-west-2',
        host='vpc-msit-zbyvohzyezkt3nr6eo5e6zcq3e.us-west-2.es.amazonaws.com')

    print 'Registering Snapshot Repository'
    resp = client.make_request(method='PUT',
                               path='/_snapshot/msit-es-index-backups',
                               data='{"type": "s3","settings": { "bucket": "msit-es-index-backups","endpoint": "s3.amazonaws.com","role_arn": "arn:aws:iam::080620772692:role/msit-es-index-backups-role"}}')
    body = resp.read()
    print body