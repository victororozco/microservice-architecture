title="VidaPlatform"

echo "$title"

command="docker-compose -f docker-compose.yml \
                  -f leads/docker-compose.yml \
                  -f auth/docker-compose.yml \
                  $1"

$command;