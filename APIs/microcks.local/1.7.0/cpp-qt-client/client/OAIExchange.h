/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIExchange.h
 *
 * Abstract representation of a Service or API exchange type (request/response, event based, ...)
 */

#ifndef OAIExchange_H
#define OAIExchange_H

#include <QJsonObject>

#include "OAIEventMessage.h"
#include "OAIRequest.h"
#include "OAIRequestResponsePair.h"
#include "OAIResponse.h"
#include "OAIUnidirectionalEvent.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRequest;
class OAIResponse;
class OAIEventMessage;

class OAIExchange : public OAIObject {
public:
    OAIExchange();
    OAIExchange(QString json);
    ~OAIExchange() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIRequest getRequest() const;
    void setRequest(const OAIRequest &request);
    bool is_request_Set() const;
    bool is_request_Valid() const;

    OAIResponse getResponse() const;
    void setResponse(const OAIResponse &response);
    bool is_response_Set() const;
    bool is_response_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    OAIEventMessage getEventMessage() const;
    void setEventMessage(const OAIEventMessage &event_message);
    bool is_event_message_Set() const;
    bool is_event_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIRequest m_request;
    bool m_request_isSet;
    bool m_request_isValid;

    OAIResponse m_response;
    bool m_response_isSet;
    bool m_response_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    OAIEventMessage m_event_message;
    bool m_event_message_isSet;
    bool m_event_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExchange)

#endif // OAIExchange_H
