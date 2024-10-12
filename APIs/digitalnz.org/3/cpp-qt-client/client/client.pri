QT += network

HEADERS += \
# Models
    $${PWD}/OAIRecord.h \
    $${PWD}/OAIRecord_locations_inner.h \
    $${PWD}/OAI_records__format__get_200_response.h \
    $${PWD}/OAI_records__record_id__more_like_this__format__get_200_response.h \
# APIs
    $${PWD}/OAIAPICallsApi.h \
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
    $${PWD}/OAIRecord.cpp \
    $${PWD}/OAIRecord_locations_inner.cpp \
    $${PWD}/OAI_records__format__get_200_response.cpp \
    $${PWD}/OAI_records__record_id__more_like_this__format__get_200_response.cpp \
# APIs
    $${PWD}/OAIAPICallsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
