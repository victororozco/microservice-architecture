title="VidaPlatform QA - Testing"

echo "$title"

command="docker stack deploy -c docker-compose.local.yml \
                  -c modules/leads/docker-compose.local.yml \
                  -c modules/auth/docker-compose.local.yml \
                  vidaplatform"

$command;