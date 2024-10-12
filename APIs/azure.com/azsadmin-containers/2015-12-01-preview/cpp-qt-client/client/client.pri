QT += network

HEADERS += \
# Models
    $${PWD}/OAIContainer.h \
    $${PWD}/OAIContainers_ListDestinationShares_200_response_inner.h \
    $${PWD}/OAIContainers_ListDestinationShares_200_response_inner_properties.h \
    $${PWD}/OAIMigrationParameters.h \
    $${PWD}/OAIMigrationResult.h \
    $${PWD}/OAIMigrationState.h \
# APIs
    $${PWD}/OAIContainersApi.h \
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
    $${PWD}/OAIContainer.cpp \
    $${PWD}/OAIContainers_ListDestinationShares_200_response_inner.cpp \
    $${PWD}/OAIContainers_ListDestinationShares_200_response_inner_properties.cpp \
    $${PWD}/OAIMigrationParameters.cpp \
    $${PWD}/OAIMigrationResult.cpp \
    $${PWD}/OAIMigrationState.cpp \
# APIs
    $${PWD}/OAIContainersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
