echo "=================================================="
echo "🚀 CMS快速清理 NCUE🚀"
echo "=================================================="

echo "⚠️ 警告: 即將刪除所有CMS設定與資料!"
echo "3秒後開始刪除"
sleep 1
echo "2秒後開始刪除"
sleep 1
echo "1秒後開始刪除"
sleep 1

echo -e "\n[1/3] 刪除CMS相關設定檔案"
sudo rm -rf /var/local/lib/cms
yes | sudo cmsDropDB  

echo -e "\n[2/3] 初始化CMS資料庫"
sudo cmsInitDB

echo -e "\n[3/3] 新增管理介面使用者(admin, admin)"
cmsAddAdmin admin -p admin