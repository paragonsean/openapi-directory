QT += network

HEADERS += \
# Models
    $${PWD}/OAIAggregateBucket.h \
    $${PWD}/OAIAggregateBy.h \
    $${PWD}/OAIAggregateRequest.h \
    $${PWD}/OAIAggregateResponse.h \
    $${PWD}/OAIApplication.h \
    $${PWD}/OAIBucketByActivity.h \
    $${PWD}/OAIBucketBySession.h \
    $${PWD}/OAIBucketByTime.h \
    $${PWD}/OAIBucketByTimePeriod.h \
    $${PWD}/OAIDataPoint.h \
    $${PWD}/OAIDataSource.h \
    $${PWD}/OAIDataType.h \
    $${PWD}/OAIDataTypeField.h \
    $${PWD}/OAIDataset.h \
    $${PWD}/OAIDevice.h \
    $${PWD}/OAIListDataPointChangesResponse.h \
    $${PWD}/OAIListDataSourcesResponse.h \
    $${PWD}/OAIListSessionsResponse.h \
    $${PWD}/OAIMapValue.h \
    $${PWD}/OAISession.h \
    $${PWD}/OAIValue.h \
    $${PWD}/OAIValueMapValEntry.h \
# APIs
    $${PWD}/OAIUsersApi.h \
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
    $${PWD}/OAIAggregateBucket.cpp \
    $${PWD}/OAIAggregateBy.cpp \
    $${PWD}/OAIAggregateRequest.cpp \
    $${PWD}/OAIAggregateResponse.cpp \
    $${PWD}/OAIApplication.cpp \
    $${PWD}/OAIBucketByActivity.cpp \
    $${PWD}/OAIBucketBySession.cpp \
    $${PWD}/OAIBucketByTime.cpp \
    $${PWD}/OAIBucketByTimePeriod.cpp \
    $${PWD}/OAIDataPoint.cpp \
    $${PWD}/OAIDataSource.cpp \
    $${PWD}/OAIDataType.cpp \
    $${PWD}/OAIDataTypeField.cpp \
    $${PWD}/OAIDataset.cpp \
    $${PWD}/OAIDevice.cpp \
    $${PWD}/OAIListDataPointChangesResponse.cpp \
    $${PWD}/OAIListDataSourcesResponse.cpp \
    $${PWD}/OAIListSessionsResponse.cpp \
    $${PWD}/OAIMapValue.cpp \
    $${PWD}/OAISession.cpp \
    $${PWD}/OAIValue.cpp \
    $${PWD}/OAIValueMapValEntry.cpp \
# APIs
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
