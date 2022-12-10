home_snapshot_ro="$(pwd)/home-20221123"
home_snapshot_rw="lair"
changes_dir="xxx"

rsync_cmd="rsync -avmh"

echo "Copying files..."
echo "$rsync_cmd --max-size=5g --compare-dest=$home_snapshot_ro/ $home_snapshot_rw/ $changes_dir/"

echo "Not Copied Files"
echo "$rsync_cmd --dry-run --compare-dest=$home_snapshot_ro/ $home_snapshot_rw/ $changes_dir/"

