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
 * OAIWarnings.h
 *
 * 
 */

#ifndef OAIWarnings_H
#define OAIWarnings_H

#include <QJsonObject>

#include "OAIWarning.h"
#include "OAIWarning_text.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWarning;
class OAIWarning_text;

class OAIWarnings : public OAIObject {
public:
    OAIWarnings();
    OAIWarnings(QString json);
    ~OAIWarnings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIWarning> getWarning() const;
    void setWarning(const QList<OAIWarning> &warning);
    bool is_warning_Set() const;
    bool is_warning_Valid() const;

    QList<OAIWarning_text> getWarningText() const;
    void setWarningText(const QList<OAIWarning_text> &warning_text);
    bool is_warning_text_Set() const;
    bool is_warning_text_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIWarning> m_warning;
    bool m_warning_isSet;
    bool m_warning_isValid;

    QList<OAIWarning_text> m_warning_text;
    bool m_warning_text_isSet;
    bool m_warning_text_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWarnings)

#endif // OAIWarnings_H
