QT += network

HEADERS += \
# Models
    $${PWD}/OAIPromotion.h \
    $${PWD}/OAIPromotion_bodyLines_inner.h \
    $${PWD}/OAIPromotion_image.h \
    $${PWD}/OAIResult.h \
    $${PWD}/OAIResult_image.h \
    $${PWD}/OAIResult_labels_inner.h \
    $${PWD}/OAISearch.h \
    $${PWD}/OAISearch_queries.h \
    $${PWD}/OAISearch_queries_nextPage_inner.h \
    $${PWD}/OAISearch_searchInformation.h \
    $${PWD}/OAISearch_spelling.h \
    $${PWD}/OAISearch_url.h \
# APIs
    $${PWD}/OAICseApi.h \
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
    $${PWD}/OAIPromotion.cpp \
    $${PWD}/OAIPromotion_bodyLines_inner.cpp \
    $${PWD}/OAIPromotion_image.cpp \
    $${PWD}/OAIResult.cpp \
    $${PWD}/OAIResult_image.cpp \
    $${PWD}/OAIResult_labels_inner.cpp \
    $${PWD}/OAISearch.cpp \
    $${PWD}/OAISearch_queries.cpp \
    $${PWD}/OAISearch_queries_nextPage_inner.cpp \
    $${PWD}/OAISearch_searchInformation.cpp \
    $${PWD}/OAISearch_spelling.cpp \
    $${PWD}/OAISearch_url.cpp \
# APIs
    $${PWD}/OAICseApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
