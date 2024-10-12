QT += network

HEADERS += \
# Models
    $${PWD}/OAIARecord.h \
    $${PWD}/OAIAaaaRecord.h \
    $${PWD}/OAICaaRecord.h \
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAICnameRecord.h \
    $${PWD}/OAIMxRecord.h \
    $${PWD}/OAINsRecord.h \
    $${PWD}/OAIPtrRecord.h \
    $${PWD}/OAIRecordSet.h \
    $${PWD}/OAIRecordSetListResult.h \
    $${PWD}/OAIRecordSetProperties.h \
    $${PWD}/OAIRecordSetUpdateParameters.h \
    $${PWD}/OAISoaRecord.h \
    $${PWD}/OAISrvRecord.h \
    $${PWD}/OAISubResource.h \
    $${PWD}/OAITxtRecord.h \
    $${PWD}/OAIZone.h \
    $${PWD}/OAIZoneListResult.h \
    $${PWD}/OAIZoneProperties.h \
    $${PWD}/OAIZoneUpdate.h \
# APIs
    $${PWD}/OAIRecordSetsApi.h \
    $${PWD}/OAIZonesApi.h \
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
    $${PWD}/OAIARecord.cpp \
    $${PWD}/OAIAaaaRecord.cpp \
    $${PWD}/OAICaaRecord.cpp \
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAICnameRecord.cpp \
    $${PWD}/OAIMxRecord.cpp \
    $${PWD}/OAINsRecord.cpp \
    $${PWD}/OAIPtrRecord.cpp \
    $${PWD}/OAIRecordSet.cpp \
    $${PWD}/OAIRecordSetListResult.cpp \
    $${PWD}/OAIRecordSetProperties.cpp \
    $${PWD}/OAIRecordSetUpdateParameters.cpp \
    $${PWD}/OAISoaRecord.cpp \
    $${PWD}/OAISrvRecord.cpp \
    $${PWD}/OAISubResource.cpp \
    $${PWD}/OAITxtRecord.cpp \
    $${PWD}/OAIZone.cpp \
    $${PWD}/OAIZoneListResult.cpp \
    $${PWD}/OAIZoneProperties.cpp \
    $${PWD}/OAIZoneUpdate.cpp \
# APIs
    $${PWD}/OAIRecordSetsApi.cpp \
    $${PWD}/OAIZonesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
