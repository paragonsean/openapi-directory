QT += network

HEADERS += \
# Models
    $${PWD}/OAIAS2Transport.h \
    $${PWD}/OAIBlobStoreTransport.h \
    $${PWD}/OAICustomConfiguration.h \
    $${PWD}/OAICustomConfiguration_transport.h \
    $${PWD}/OAIDestination.h \
    $${PWD}/OAIDetail.h \
    $${PWD}/OAIItemRouting.h \
    $${PWD}/OAINullTransport.h \
    $${PWD}/OAIOrganization.h \
    $${PWD}/OAIReceiver.h \
    $${PWD}/OAIReceiver_jurisdictionalFilters_inner.h \
    $${PWD}/OAIReceiver_timing.h \
    $${PWD}/OAIReceiver_translations_inner.h \
    $${PWD}/OAIRedoxTransport.h \
    $${PWD}/OAIReport.h \
    $${PWD}/OAISFTPTransport.h \
    $${PWD}/OAISender.h \
    $${PWD}/OAISettingMetadata.h \
    $${PWD}/OAIStandardHL7Configuration.h \
    $${PWD}/OAIStandardHL7Configuration_transport.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAS2Transport.cpp \
    $${PWD}/OAIBlobStoreTransport.cpp \
    $${PWD}/OAICustomConfiguration.cpp \
    $${PWD}/OAICustomConfiguration_transport.cpp \
    $${PWD}/OAIDestination.cpp \
    $${PWD}/OAIDetail.cpp \
    $${PWD}/OAIItemRouting.cpp \
    $${PWD}/OAINullTransport.cpp \
    $${PWD}/OAIOrganization.cpp \
    $${PWD}/OAIReceiver.cpp \
    $${PWD}/OAIReceiver_jurisdictionalFilters_inner.cpp \
    $${PWD}/OAIReceiver_timing.cpp \
    $${PWD}/OAIReceiver_translations_inner.cpp \
    $${PWD}/OAIRedoxTransport.cpp \
    $${PWD}/OAIReport.cpp \
    $${PWD}/OAISFTPTransport.cpp \
    $${PWD}/OAISender.cpp \
    $${PWD}/OAISettingMetadata.cpp \
    $${PWD}/OAIStandardHL7Configuration.cpp \
    $${PWD}/OAIStandardHL7Configuration_transport.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
