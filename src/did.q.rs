complexity:

1. JSONPath (~2,000–4,000 lines)
    * Tokenizer
    * Parser
    * AST
    * Evaluator
    * Recursive descent
    * Filters
    * Wildcards
    * Slices
    * Tests
2. JMESPath (~4,000–8,000 lines)
    * Expression parser
    * Function library
    * Pipes
    * Projections
    * Filters
    * Multi-select
    * Tests
3. jq (~8,000–15,000 lines)
    * Lexer
    * Parser
    * Filter engine
    * Streaming
    * Transformations
    * Variables
    * Functions
    * Modules
4. SQL (~15,000–30,000 lines)
    * SQL lexer
    * SQL parser
    * AST
    * Query planner
    * JOINs
    * GROUP BY
    * ORDER BY
    * Aggregates
    * Subqueries
    * Optimizer
5. JSONiq (~15,000–25,000 lines)
    * FLWOR expressions
    * Functions
    * Updates
    * JSON constructors
    * Type system
    * Optimizer
6. GraphQL (~10,000–20,000 lines)
    * SDL parser
    * Schema builder
    * Query parser
    * Validation
    * Resolver engine
    * Introspection
    * Subscriptions (optional)

Once these are complete, you can unify them behind a single interface:

const engine = new QueryEngine();
engine.execute({
    language: "sql",
    query: "...",
    data
});
engine.execute({
    language: "jsoniq",
    query: "...",
    data
});
engine.execute({
    language: "jsonpath",
    query: "...",
    data
});
engine.execute({
    language: "jmespath",
    query: "...",
    data
});
engine.execute({
    language: "graphql",
    query: "...",
    data
});
engine.execute({
    language: "jq",
    query: "...",
    data
});
