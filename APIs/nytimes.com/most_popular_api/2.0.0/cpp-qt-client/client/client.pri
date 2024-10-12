QT += network

HEADERS += \
# Models
    $${PWD}/OAIArticle.h \
    $${PWD}/OAIArticleWithCountType.h \
    $${PWD}/OAIArticleWithCountType_media_inner.h \
    $${PWD}/OAIArticleWithCountType_media_inner_media_metadata.h \
    $${PWD}/OAIGET_mostemailed_section_time_period_json_200_response.h \
    $${PWD}/OAIGET_mostemailed_section_time_period_json_400_response.h \
    $${PWD}/OAIGET_mostshared_section_time_period_json_200_response.h \
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
    $${PWD}/OAIArticle.cpp \
    $${PWD}/OAIArticleWithCountType.cpp \
    $${PWD}/OAIArticleWithCountType_media_inner.cpp \
    $${PWD}/OAIArticleWithCountType_media_inner_media_metadata.cpp \
    $${PWD}/OAIGET_mostemailed_section_time_period_json_200_response.cpp \
    $${PWD}/OAIGET_mostemailed_section_time_period_json_400_response.cpp \
    $${PWD}/OAIGET_mostshared_section_time_period_json_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
