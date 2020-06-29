title="VidaPlatform - Localhost"

echo "$title"

command="docker-compose -f docker-compose.local.yml \
                  -f modules/leads/docker-compose.local.yml \
                  -f modules/auth/docker-compose.local.yml \
                  $1"

$command;