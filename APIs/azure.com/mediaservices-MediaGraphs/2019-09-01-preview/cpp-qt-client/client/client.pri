QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiError.h \
    $${PWD}/OAIMediaGraph.h \
    $${PWD}/OAIMediaGraphAssetSink.h \
    $${PWD}/OAIMediaGraphCollection.h \
    $${PWD}/OAIMediaGraphOperationError.h \
    $${PWD}/OAIMediaGraphOperationStatus.h \
    $${PWD}/OAIMediaGraphProperties.h \
    $${PWD}/OAIMediaGraphRtspSource.h \
    $${PWD}/OAIMediaGraphSink.h \
    $${PWD}/OAIMediaGraphSource.h \
    $${PWD}/OAIMediaGraphUserCredentials.h \
    $${PWD}/OAIODataError.h \
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
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAIMediaGraph.cpp \
    $${PWD}/OAIMediaGraphAssetSink.cpp \
    $${PWD}/OAIMediaGraphCollection.cpp \
    $${PWD}/OAIMediaGraphOperationError.cpp \
    $${PWD}/OAIMediaGraphOperationStatus.cpp \
    $${PWD}/OAIMediaGraphProperties.cpp \
    $${PWD}/OAIMediaGraphRtspSource.cpp \
    $${PWD}/OAIMediaGraphSink.cpp \
    $${PWD}/OAIMediaGraphSource.cpp \
    $${PWD}/OAIMediaGraphUserCredentials.cpp \
    $${PWD}/OAIODataError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
