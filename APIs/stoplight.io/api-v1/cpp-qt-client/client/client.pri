QT += network

HEADERS += \
# Models
    $${PWD}/OAIGET_versions_versionId_export_format_200_response.h \
    $${PWD}/OAIPOST_versions_publish_anon_200_response.h \
    $${PWD}/OAIPOST_versions_publish_anon_request.h \
    $${PWD}/OAIPOST_versions_publish_anon_request_specData.h \
    $${PWD}/OAIPOST_versions_versionId_publish_200_response.h \
    $${PWD}/OAIPUT_versions_versionId_import_200_response.h \
    $${PWD}/OAIPUT_versions_versionId_import_200_response_data.h \
    $${PWD}/OAIPUT_versions_versionId_import_request.h \
    $${PWD}/OAIPUT_versions_versionId_import_request_options.h \
    $${PWD}/OAIPUT_versions_versionId_unpublish_200_response.h \
    $${PWD}/OAIShared_user.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIVersionsApi.h \
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
    $${PWD}/OAIGET_versions_versionId_export_format_200_response.cpp \
    $${PWD}/OAIPOST_versions_publish_anon_200_response.cpp \
    $${PWD}/OAIPOST_versions_publish_anon_request.cpp \
    $${PWD}/OAIPOST_versions_publish_anon_request_specData.cpp \
    $${PWD}/OAIPOST_versions_versionId_publish_200_response.cpp \
    $${PWD}/OAIPUT_versions_versionId_import_200_response.cpp \
    $${PWD}/OAIPUT_versions_versionId_import_200_response_data.cpp \
    $${PWD}/OAIPUT_versions_versionId_import_request.cpp \
    $${PWD}/OAIPUT_versions_versionId_import_request_options.cpp \
    $${PWD}/OAIPUT_versions_versionId_unpublish_200_response.cpp \
    $${PWD}/OAIShared_user.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIVersionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
