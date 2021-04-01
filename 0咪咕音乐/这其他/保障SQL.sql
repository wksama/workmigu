-- 根据专辑ID，查询专辑素材数据，主要观察album_name 、album_type 、tags（是否包含不展示标签）、object_state(0：正常，非0：下架\隐藏)
SELECT * FROM material_album WHERE album_id  in('1136519316','1136517413');

-- 根据专辑ID，查询专辑索引数据，主要观察album_type、publish_date、presell_date、presell_state、first_start_date、first_end_date、first_start_state、is_enabled、is_computed、is_deleted
SELECT id,name,album_type,publish_date,presell_date,presell_state,first_start_date,first_end_date,first_start_state,is_enabled,is_computed,is_deleted,create_time,update_time FROM index_album WHERE id in('1136529480','1136517413');

-- 根据专辑ID，查询专辑关联歌曲素材数据，主要观察song_name、object_state(0：正常，非0：下架\隐藏)
SELECT sa.album_id,s.* FROM relation_song_album sa left JOIN material_song s on sa.song_id = s.song_id WHERE sa.album_id in('1136519316','1136517413') and sa.is_deleted = 0;

-- 根据专辑ID，查询专辑关联歌曲索引数据，主要观察is_copyright、、product_info、first_start_state、is_hot_data、is_enabled、is_computed、is_deleted
SELECT sa.album_id,s.id,s.name,s.is_copyright,s.product_info,s.channels,s.hot,s.hot_level,s.singer_ids,s.singer_names,s.singer_info,s.album_names,s.album_info,s.first_start_state,s.is_hot_data,s.is_enabled,s.is_computed,s.is_deleted FROM relation_song_album sa left JOIN index_song s on sa.song_id = s.id WHERE sa.album_id in('1136519316','1136517413') and sa.is_deleted = 0;

-- 根据版权ID，查询歌曲索引数据
SELECT s.id,s.name,s.is_copyright,s.product_info,s.channels,s.hot,s.hot_level,s.singer_ids,s.singer_names,s.singer_info,s.album_names,s.album_info,s.first_start_state,s.is_hot_data,s.is_enabled,s.is_computed,s.is_deleted FROM cataloginfo c left JOIN index_song s on c.material_id = s.id WHERE c.copyright_id in('69905304552','69905304551') and c.object_state = 0;

-- 根据专辑ID，查询歌曲全曲产品数据（查询全产品最后的content_type = 2条件去掉），主要观察content_id、copyright_id、content_type、invalidate_date、validate_date、param_set、show_time、object_state(0：正常，非0：下架\隐藏)
SELECT content_id,copyright_id,content_type,content_name,invalidate_date,validate_date,param_set,show_time,object_state,create_time,update_time FROM product_wireless WHERE copyright_id in (SELECT copyright_id FROM cataloginfo WHERE material_id in (SELECT song_id FROM relation_song_album WHERE album_id in('1136519316','1136517413') and is_deleted =0)) and content_type = 2; 

-- 根据产品ID，查询歌曲产品数据
-- SELECT content_id,copyright_id,content_type,content_name,invalidate_date,validate_date,param_set,show_time,object_state,create_time,update_time FROM product_wireless WHERE content_id in ('600919000002324184','600919000002324189','600919000002324194','600919000002324199','600919000002324204','600919000002324209'); 

-- 根据版权ID，查询歌曲产品数据
-- SELECT content_id,copyright_id,content_type,content_name,invalidate_date,validate_date,param_set,show_time,object_state,create_time,update_time FROM product_wireless WHERE copyright_id in ('60091900044','60091900045'); 

-- 手动修改全曲产品show_time
-- update product_wireless set param_set = replace(param_set,'2020-11-24 00:00:00','2020-11-23 23:51:00') , show_time = '2020-11-23 23:51:00' WHERE copyright_id in (SELECT copyright_id FROM cataloginfo WHERE material_id in (SELECT song_id FROM relation_song_album WHERE album_id = '1136187705')) and content_type = 2;









