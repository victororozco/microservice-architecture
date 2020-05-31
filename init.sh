title="Vidaplatform menú"
prompt="Pick an option:"
options=(
  "Build" \
  "Up" \
  "Down"
)

echo "$title"
PS3="$prompt "

build="docker-compose -f docker-compose.yml \
                  -f leads/docker-compose.yml \
                  build"

up="docker-compose -f docker-compose.yml \
                  -f leads/docker-compose.yml \
                  up"

down="docker-compose -f docker-compose.yml \
                  -f leads/docker-compose.yml \
                  down"


select opt in "${options[@]}" "Quit"; do 

    case "$REPLY" in
      1 ) $UP; break;;
      2 ) $up; break;;
      3 ) $down; break;;

      $(( ${#options[@]}+1 )) ) echo "Goodbye!"; break;;
      *) echo "Invalid option. Try another one.";continue;;

    esac

done