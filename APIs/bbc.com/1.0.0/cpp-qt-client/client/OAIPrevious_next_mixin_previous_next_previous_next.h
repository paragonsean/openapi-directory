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
 * OAIPrevious_next_mixin_previous_next_previous_next.h
 *
 * 
 */

#ifndef OAIPrevious_next_mixin_previous_next_previous_next_H
#define OAIPrevious_next_mixin_previous_next_previous_next_H

#include <QJsonObject>

#include "OAIReference.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIReference;

class OAIPrevious_next_mixin_previous_next_previous_next : public OAIObject {
public:
    OAIPrevious_next_mixin_previous_next_previous_next();
    OAIPrevious_next_mixin_previous_next_previous_next(QString json);
    ~OAIPrevious_next_mixin_previous_next_previous_next() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIReference getNext() const;
    void setNext(const OAIReference &next);
    bool is_next_Set() const;
    bool is_next_Valid() const;

    OAIReference getPrevious() const;
    void setPrevious(const OAIReference &previous);
    bool is_previous_Set() const;
    bool is_previous_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIReference m_next;
    bool m_next_isSet;
    bool m_next_isValid;

    OAIReference m_previous;
    bool m_previous_isSet;
    bool m_previous_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPrevious_next_mixin_previous_next_previous_next)

#endif // OAIPrevious_next_mixin_previous_next_previous_next_H
