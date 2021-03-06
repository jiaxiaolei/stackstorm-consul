from lib import action


class ConsulAclCreateAction(action.ConsulBaseAction):
    def run(
        self,
        consul_profile=None,
        name=None,
        acl_type="client",
        rules=None,
        token=None,
        acl_id=None
    ):
        self._create_client(consul_profile)

        # Action parameter "token" defaults to an empty string when no input is provided.
        # Consul-Python tests for None to use the agent's token, so "token" set to None here.
        if token == "":
            token = None

        rules = rules.encode("ascii", "ignore")
        return (
            True,
            self.consul.acl.create(
                name=name,
                type=acl_type,
                rules=rules,
                acl_id=acl_id,
                token=token
            )
        )
