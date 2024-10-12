

# LinodeBackupsSchedule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**day** | [**DayEnum**](#DayEnum) | The day of the week that your Linode&#39;s weekly Backup is taken. If not set manually, a day will be chosen for you. Backups are taken every day, but backups taken on this day are preferred when selecting backups to retain for a longer period.   If not set manually, then when backups are initially enabled, this may come back as &#x60;Scheduling&#x60; until the &#x60;day&#x60; is automatically selected.  |  [optional] |
|**window** | [**WindowEnum**](#WindowEnum) | The window in which your backups will be taken, in UTC. A backups window is a two-hour span of time in which the backup may occur.   For example, &#x60;W10&#x60; indicates that your backups should be taken between 10:00 and 12:00. If you do not choose a backup window, one will be selected for you automatically.   If not set manually, when backups are initially enabled this may come back as &#x60;Scheduling&#x60; until the &#x60;window&#x60; is automatically selected.  |  [optional] |



## Enum: DayEnum

| Name | Value |
|---- | -----|
| SCHEDULING | &quot;Scheduling&quot; |
| SUNDAY | &quot;Sunday&quot; |
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| SATURDAY | &quot;Saturday&quot; |



## Enum: WindowEnum

| Name | Value |
|---- | -----|
| SCHEDULING | &quot;Scheduling&quot; |
| W0 | &quot;W0&quot; |
| W2 | &quot;W2&quot; |
| W4 | &quot;W4&quot; |
| W6 | &quot;W6&quot; |
| W8 | &quot;W8&quot; |
| W10 | &quot;W10&quot; |
| W12 | &quot;W12&quot; |
| W14 | &quot;W14&quot; |
| W16 | &quot;W16&quot; |
| W18 | &quot;W18&quot; |
| W20 | &quot;W20&quot; |
| W22 | &quot;W22&quot; |



