QT += network

HEADERS += \
# Models
    $${PWD}/OAIARecord.h \
    $${PWD}/OAIAaaaRecord.h \
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAICnameRecord.h \
    $${PWD}/OAIMxRecord.h \
    $${PWD}/OAIPrivateZone.h \
    $${PWD}/OAIPrivateZoneListResult.h \
    $${PWD}/OAIPrivateZoneProperties.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIPtrRecord.h \
    $${PWD}/OAIRecordSet.h \
    $${PWD}/OAIRecordSetListResult.h \
    $${PWD}/OAIRecordSetProperties.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISoaRecord.h \
    $${PWD}/OAISrvRecord.h \
    $${PWD}/OAISubResource.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAITxtRecord.h \
    $${PWD}/OAIVirtualNetworkLink.h \
    $${PWD}/OAIVirtualNetworkLinkListResult.h \
    $${PWD}/OAIVirtualNetworkLinkProperties.h \
# APIs
    $${PWD}/OAIPrivateZonesApi.h \
    $${PWD}/OAIRecordSetsApi.h \
    $${PWD}/OAIVirtualNetworkLinksApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAICnameRecord.cpp \
    $${PWD}/OAIMxRecord.cpp \
    $${PWD}/OAIPrivateZone.cpp \
    $${PWD}/OAIPrivateZoneListResult.cpp \
    $${PWD}/OAIPrivateZoneProperties.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIPtrRecord.cpp \
    $${PWD}/OAIRecordSet.cpp \
    $${PWD}/OAIRecordSetListResult.cpp \
    $${PWD}/OAIRecordSetProperties.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISoaRecord.cpp \
    $${PWD}/OAISrvRecord.cpp \
    $${PWD}/OAISubResource.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAITxtRecord.cpp \
    $${PWD}/OAIVirtualNetworkLink.cpp \
    $${PWD}/OAIVirtualNetworkLinkListResult.cpp \
    $${PWD}/OAIVirtualNetworkLinkProperties.cpp \
# APIs
    $${PWD}/OAIPrivateZonesApi.cpp \
    $${PWD}/OAIRecordSetsApi.cpp \
    $${PWD}/OAIVirtualNetworkLinksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
