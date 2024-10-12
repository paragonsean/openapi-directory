QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckValidCredsResponse.h \
    $${PWD}/OAIDataSource.h \
    $${PWD}/OAIDataSourceParameter.h \
    $${PWD}/OAIEmailPreferences.h \
    $${PWD}/OAIEncryptionConfiguration.h \
    $${PWD}/OAIEnrollDataSourcesRequest.h \
    $${PWD}/OAIListDataSourcesResponse.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListTransferConfigsResponse.h \
    $${PWD}/OAIListTransferLogsResponse.h \
    $${PWD}/OAIListTransferRunsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIScheduleOptions.h \
    $${PWD}/OAIScheduleTransferRunsRequest.h \
    $${PWD}/OAIScheduleTransferRunsResponse.h \
    $${PWD}/OAIStartManualTransferRunsRequest.h \
    $${PWD}/OAIStartManualTransferRunsResponse.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITimeRange.h \
    $${PWD}/OAITransferConfig.h \
    $${PWD}/OAITransferMessage.h \
    $${PWD}/OAITransferRun.h \
    $${PWD}/OAIUnenrollDataSourcesRequest.h \
    $${PWD}/OAIUserInfo.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAICheckValidCredsResponse.cpp \
    $${PWD}/OAIDataSource.cpp \
    $${PWD}/OAIDataSourceParameter.cpp \
    $${PWD}/OAIEmailPreferences.cpp \
    $${PWD}/OAIEncryptionConfiguration.cpp \
    $${PWD}/OAIEnrollDataSourcesRequest.cpp \
    $${PWD}/OAIListDataSourcesResponse.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListTransferConfigsResponse.cpp \
    $${PWD}/OAIListTransferLogsResponse.cpp \
    $${PWD}/OAIListTransferRunsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIScheduleOptions.cpp \
    $${PWD}/OAIScheduleTransferRunsRequest.cpp \
    $${PWD}/OAIScheduleTransferRunsResponse.cpp \
    $${PWD}/OAIStartManualTransferRunsRequest.cpp \
    $${PWD}/OAIStartManualTransferRunsResponse.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITimeRange.cpp \
    $${PWD}/OAITransferConfig.cpp \
    $${PWD}/OAITransferMessage.cpp \
    $${PWD}/OAITransferRun.cpp \
    $${PWD}/OAIUnenrollDataSourcesRequest.cpp \
    $${PWD}/OAIUserInfo.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
