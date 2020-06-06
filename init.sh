title="VidaPlatform"

echo "$title"

command="docker-compose -f docker-compose.yml \
                  -f modules/leads/docker-compose.yml \
                  -f modules/auth/docker-compose.yml \
                  $1"

$command;