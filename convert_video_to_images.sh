for folder in $1/*
do
    for file in "$folder"/*.avi
    do
        # shellcheck disable=SC2199
        if [[ ! -d "${file[@]%.avi}" ]]; then
            mkdir -p "${file[@]%.avi}"
        fi
        # shellcheck disable=SC2145
        F:/ffmpeg-4.2.1-win64-static/bin/ffmpeg -i "$file" -vf fps=$2 "${file[@]%.avi}"/%05d.jpg
        rm "$file"
    done
done