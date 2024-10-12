/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIVersion_availability.h
 *
 * 
 */

#ifndef OAIVersion_availability_H
#define OAIVersion_availability_H

#include <QJsonObject>

#include "OAIVersion_availability_availability.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIVersion_availability_availability;

class OAIVersion_availability : public OAIObject {
public:
    OAIVersion_availability();
    OAIVersion_availability(QString json);
    ~OAIVersion_availability() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIVersion_availability_availability getAvailability() const;
    void setAvailability(const OAIVersion_availability_availability &availability);
    bool is_availability_Set() const;
    bool is_availability_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIVersion_availability_availability m_availability;
    bool m_availability_isSet;
    bool m_availability_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVersion_availability)

#endif // OAIVersion_availability_H
