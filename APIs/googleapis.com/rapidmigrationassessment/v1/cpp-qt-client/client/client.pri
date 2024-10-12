QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnnotation.h \
    $${PWD}/OAICollector.h \
    $${PWD}/OAIGuestOsScan.h \
    $${PWD}/OAIListCollectorsResponse.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationMetadata.h \
    $${PWD}/OAIPauseCollectorRequest.h \
    $${PWD}/OAIRegisterCollectorRequest.h \
    $${PWD}/OAIResumeCollectorRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIVSphereScan.h \
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
    $${PWD}/OAIAnnotation.cpp \
    $${PWD}/OAICollector.cpp \
    $${PWD}/OAIGuestOsScan.cpp \
    $${PWD}/OAIListCollectorsResponse.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationMetadata.cpp \
    $${PWD}/OAIPauseCollectorRequest.cpp \
    $${PWD}/OAIRegisterCollectorRequest.cpp \
    $${PWD}/OAIResumeCollectorRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIVSphereScan.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
