QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_errors_inner.h \
    $${PWD}/OAIFile.h \
    $${PWD}/OAIFile_attributes.h \
    $${PWD}/OAILine.h \
    $${PWD}/OAILine_attributes.h \
    $${PWD}/OAILine_attributes_identified_fields_inner.h \
    $${PWD}/OAIOccurrence.h \
    $${PWD}/OAIOccurrence_attributes.h \
    $${PWD}/OAI_file__fileId__lines_get_200_response.h \
    $${PWD}/OAI_file__fileId__occurrences_get_200_response.h \
    $${PWD}/OAI_file_post_200_response.h \
# APIs
    $${PWD}/OAIFileApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_errors_inner.cpp \
    $${PWD}/OAIFile.cpp \
    $${PWD}/OAIFile_attributes.cpp \
    $${PWD}/OAILine.cpp \
    $${PWD}/OAILine_attributes.cpp \
    $${PWD}/OAILine_attributes_identified_fields_inner.cpp \
    $${PWD}/OAIOccurrence.cpp \
    $${PWD}/OAIOccurrence_attributes.cpp \
    $${PWD}/OAI_file__fileId__lines_get_200_response.cpp \
    $${PWD}/OAI_file__fileId__occurrences_get_200_response.cpp \
    $${PWD}/OAI_file_post_200_response.cpp \
# APIs
    $${PWD}/OAIFileApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
