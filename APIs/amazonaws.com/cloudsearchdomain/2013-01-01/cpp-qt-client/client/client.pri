QT += network

HEADERS += \
# Models
    $${PWD}/OAIBucket.h \
    $${PWD}/OAIBucketInfo.h \
    $${PWD}/OAIContentType.h \
    $${PWD}/OAIDocumentServiceException.h \
    $${PWD}/OAIDocumentServiceWarning.h \
    $${PWD}/OAIFieldStats.h \
    $${PWD}/OAIHit.h \
    $${PWD}/OAIHits.h \
    $${PWD}/OAIQueryParser.h \
    $${PWD}/OAISearchException.h \
    $${PWD}/OAISearchResponse.h \
    $${PWD}/OAISearchResponse_hits.h \
    $${PWD}/OAISearchResponse_status.h \
    $${PWD}/OAISearchStatus.h \
    $${PWD}/OAISuggestModel.h \
    $${PWD}/OAISuggestResponse.h \
    $${PWD}/OAISuggestResponse_status.h \
    $${PWD}/OAISuggestResponse_suggest.h \
    $${PWD}/OAISuggestStatus.h \
    $${PWD}/OAISuggestionMatch.h \
    $${PWD}/OAIUploadDocumentsRequest.h \
    $${PWD}/OAIUploadDocumentsResponse.h \
    $${PWD}/OAIUploadDocuments_request.h \
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
    $${PWD}/OAIBucket.cpp \
    $${PWD}/OAIBucketInfo.cpp \
    $${PWD}/OAIContentType.cpp \
    $${PWD}/OAIDocumentServiceException.cpp \
    $${PWD}/OAIDocumentServiceWarning.cpp \
    $${PWD}/OAIFieldStats.cpp \
    $${PWD}/OAIHit.cpp \
    $${PWD}/OAIHits.cpp \
    $${PWD}/OAIQueryParser.cpp \
    $${PWD}/OAISearchException.cpp \
    $${PWD}/OAISearchResponse.cpp \
    $${PWD}/OAISearchResponse_hits.cpp \
    $${PWD}/OAISearchResponse_status.cpp \
    $${PWD}/OAISearchStatus.cpp \
    $${PWD}/OAISuggestModel.cpp \
    $${PWD}/OAISuggestResponse.cpp \
    $${PWD}/OAISuggestResponse_status.cpp \
    $${PWD}/OAISuggestResponse_suggest.cpp \
    $${PWD}/OAISuggestStatus.cpp \
    $${PWD}/OAISuggestionMatch.cpp \
    $${PWD}/OAIUploadDocumentsRequest.cpp \
    $${PWD}/OAIUploadDocumentsResponse.cpp \
    $${PWD}/OAIUploadDocuments_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
