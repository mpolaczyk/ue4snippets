#!/usr/bin/env python

from delegatesGenerator import Delegate


class DelegateSnippet:

    def __init__(self, title, author, description, shortcut, delegateKind, delegateOwningType, delegateParamNames, delegateParamTypes):
        self.title = title
        self.author = author
        self.description = description
        self.shortcut = shortcut
        self.delegateKind = delegateKind
        self.delegateOwningType = delegateOwningType
        self.delegateParamNames = delegateParamNames
        self.delegateParamTypes = delegateParamTypes

    def Generate(self):
        a = '<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\
        <CodeSnippets xmlns=\"http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet\">\n\
          <CodeSnippet Format=\"1.0.0\">\n\
            <Header>\n\
              <SnippetTypes>\n\
                <SnippetType>Expansion</SnippetType>\n\
              </SnippetTypes>\n\
              <Title>{title}</Title>\n\
              <Author>{author}</Author>\n\
              <Description>{description}</Description>\n\
              <HelpUrl>\n\
              </HelpUrl>\n\
              <Shortcut>{shortcut}</Shortcut>\n\
            </Header>\n\
            <Snippet>\n\
              <Declarations>\n'.format(title=self.title, author=self.author, description=self.description, shortcut=self.shortcut)	  
        b = '<Literal Editable=\"true\">\n\
          <ID>$delegateName$</ID>\n\
          <ToolTip>Delegate type name</ToolTip>\n\
          <Default>DelegateName</Default>\n\
          <Function>\n\
          </Function>\n\
        </Literal>\n'
        c = '<Literal Editable=\"true\">\n\
          <ID>$owningType$</ID>\n\
          <ToolTip>Delegate owning type name</ToolTip>\n\
          <Default>OwningType</Default>\n\
          <Function>\n\
          </Function>\n\
        </Literal>\n'
        d = ''
        for p in range(1, self.delegateParamNames+1):
            d += '<Literal Editable=\"true\">\n\
              <ID>$paramName{0}$</ID>\n\
              <ToolTip>Parameter name</ToolTip>\n\
              <Default>Param{1}Name</Default>\n\
              <Function>\n\
              </Function>\n\
            </Literal>\n'.format(p,p)
        e = ''
        for p in range(1, self.delegateParamTypes+1):
            e += '<Literal Editable=\"true\">\n\
              <ID>$paramType{0}$</ID>\n\
              <ToolTip>Parameter type</ToolTip>\n\
              <Default>Param{1}type</Default>\n\
              <Function>\n\
              </Function>\n\
            </Literal>\n'.format(p,p)
        f = '</Declarations>\n\
              <Code Language=\"cpp\"><![CDATA['
        g = Delegate(self.delegateKind, '$delegateName$', self.delegateOwningType, ['$$paramName{0}$$'.format(p) for p in range(1,self.delegateParamNames+1)], ['$$paramType{0}$$'.format(p) for p in range(1,self.delegateParamTypes+1)]).Generate()
        h = '$selected$ $end$]]></Code>\n\
            </Snippet>\n\
          </CodeSnippet>\n\
        </CodeSnippets>'        
        out = [a, b, c, d, e, f, g, h]
        return ''.join(out)












