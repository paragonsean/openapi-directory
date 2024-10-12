QT += network

HEADERS += \
# Models
    $${PWD}/OAIFrontline_v1_user.h \
    $${PWD}/OAIUser_enum_state_type.h \
# APIs
    $${PWD}/OAIFrontlineV1UserApi.h \
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
    $${PWD}/OAIFrontline_v1_user.cpp \
    $${PWD}/OAIUser_enum_state_type.cpp \
# APIs
    $${PWD}/OAIFrontlineV1UserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
