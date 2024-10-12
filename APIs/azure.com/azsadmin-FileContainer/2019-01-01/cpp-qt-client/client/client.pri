QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorInfo.h \
    $${PWD}/OAIFileContainer.h \
    $${PWD}/OAIFileContainerAdminProperties.h \
    $${PWD}/OAIFileContainerParameters.h \
    $${PWD}/OAIFileContainersList.h \
    $${PWD}/OAIPostCopyAction.h \
# APIs
    $${PWD}/OAIFileContainersApi.h \
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
    $${PWD}/OAIErrorInfo.cpp \
    $${PWD}/OAIFileContainer.cpp \
    $${PWD}/OAIFileContainerAdminProperties.cpp \
    $${PWD}/OAIFileContainerParameters.cpp \
    $${PWD}/OAIFileContainersList.cpp \
    $${PWD}/OAIPostCopyAction.cpp \
# APIs
    $${PWD}/OAIFileContainersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
