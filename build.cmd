@echo off
echo .
echo ############################
echo #      BUILDING CLIENT     #
echo ############################
echo .

pyinstaller --specpath "build/client/spec" --distpath "dist" --workpath "build/client" --noconfirm --onefile --windowed "client/client.py" 

echo .
echo ############################
echo #        BUILD DONE        #
echo ############################
echo .

echo .
echo ############################
echo #      BUILDING SERVER     #
echo ############################
echo .

pyinstaller --specpath "build/server/spec" --distpath "dist" --workpath "build/server" --noconfirm --onefile --console "server/server.py"

echo .
echo ############################
echo #        BUILD DONE        #
echo ############################
echo .