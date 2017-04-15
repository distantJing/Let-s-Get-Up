## 触摸屏 HDMI使用注意事项 ##
#### 用户名pi，默认密码raspberry ####
### 切换方法 ###

	cd到LCD-show目录下
	切换到触摸屏输出：sudo ./LCD35-show
	切换到HDMI输出：sudo ./LCD-hdmi

### 注意 ###
     每次关机前请务必切换到触摸屏输出方式
     否则下次开机二者都无法接受到信号
### 若关机状态为HDMI输出，下次开机需 ###
     使用putty远程连接方式，进行1中所述操作

## 树莓派进入emergency mode ##
	umount /dev/mmcblk0p2
	e2fsck -f -y -v -C 0 /dev/mmcblk0p2
	reboot
