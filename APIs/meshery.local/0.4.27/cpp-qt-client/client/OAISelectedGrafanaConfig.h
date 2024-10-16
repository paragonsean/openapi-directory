/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISelectedGrafanaConfig.h
 *
 * SelectedGrafanaConfig represents the selected boards, panels, and template variables
 */

#ifndef OAISelectedGrafanaConfig_H
#define OAISelectedGrafanaConfig_H

#include <QJsonObject>

#include "OAIGrafanaBoard.h"
#include "OAIPanel.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGrafanaBoard;
class OAIPanel;

class OAISelectedGrafanaConfig : public OAIObject {
public:
    OAISelectedGrafanaConfig();
    OAISelectedGrafanaConfig(QString json);
    ~OAISelectedGrafanaConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGrafanaBoard getBoard() const;
    void setBoard(const OAIGrafanaBoard &board);
    bool is_board_Set() const;
    bool is_board_Valid() const;

    QList<OAIPanel> getPanels() const;
    void setPanels(const QList<OAIPanel> &panels);
    bool is_panels_Set() const;
    bool is_panels_Valid() const;

    QList<QString> getTemplateVars() const;
    void setTemplateVars(const QList<QString> &template_vars);
    bool is_template_vars_Set() const;
    bool is_template_vars_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGrafanaBoard m_board;
    bool m_board_isSet;
    bool m_board_isValid;

    QList<OAIPanel> m_panels;
    bool m_panels_isSet;
    bool m_panels_isValid;

    QList<QString> m_template_vars;
    bool m_template_vars_isSet;
    bool m_template_vars_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISelectedGrafanaConfig)

#endif // OAISelectedGrafanaConfig_H
