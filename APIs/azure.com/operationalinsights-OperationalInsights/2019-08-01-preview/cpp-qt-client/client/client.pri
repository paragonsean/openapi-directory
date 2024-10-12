QT += network

HEADERS += \
# Models
    $${PWD}/OAIDataExport.h \
    $${PWD}/OAIDataExportListResult.h \
    $${PWD}/OAIDataExportProperties.h \
    $${PWD}/OAIDestination.h \
    $${PWD}/OAIDestinationMetaData.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIProxyResource.h \
# APIs
    $${PWD}/OAIDataExportApi.h \
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
    $${PWD}/OAIDataExport.cpp \
    $${PWD}/OAIDataExportListResult.cpp \
    $${PWD}/OAIDataExportProperties.cpp \
    $${PWD}/OAIDestination.cpp \
    $${PWD}/OAIDestinationMetaData.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIProxyResource.cpp \
# APIs
    $${PWD}/OAIDataExportApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
