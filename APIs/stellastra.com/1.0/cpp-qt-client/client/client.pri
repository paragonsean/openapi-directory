QT += network

HEADERS += \
# Models
    $${PWD}/OAI_post_review_post_200_response.h \
    $${PWD}/OAI_post_review_post_400_response.h \
    $${PWD}/OAI_post_review_post_401_response.h \
    $${PWD}/OAI_post_review_post_403_response.h \
    $${PWD}/OAI_post_review_post_request.h \
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
    $${PWD}/OAI_post_review_post_200_response.cpp \
    $${PWD}/OAI_post_review_post_400_response.cpp \
    $${PWD}/OAI_post_review_post_401_response.cpp \
    $${PWD}/OAI_post_review_post_403_response.cpp \
    $${PWD}/OAI_post_review_post_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
