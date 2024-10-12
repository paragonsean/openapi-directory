QT += network

HEADERS += \
# Models
    $${PWD}/OAITagsResource.h \
    $${PWD}/OAIWebTest.h \
    $${PWD}/OAIWebTestGeolocation.h \
    $${PWD}/OAIWebTestListResult.h \
    $${PWD}/OAIWebTestProperties.h \
    $${PWD}/OAIWebTestProperties_Configuration.h \
    $${PWD}/OAIWebtestsResource.h \
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
    $${PWD}/OAITagsResource.cpp \
    $${PWD}/OAIWebTest.cpp \
    $${PWD}/OAIWebTestGeolocation.cpp \
    $${PWD}/OAIWebTestListResult.cpp \
    $${PWD}/OAIWebTestProperties.cpp \
    $${PWD}/OAIWebTestProperties_Configuration.cpp \
    $${PWD}/OAIWebtestsResource.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
