package osdd_test

import (
	"os"
	"testing"

	"google.golang.org/protobuf/encoding/protojson"

	"github.com/opensdd/osdd-api/clients/go/osdd/recipes"
)

func TestParseExampleJSON(t *testing.T) {
	data, err := os.ReadFile("testdata/example.json")
	if err != nil {
		t.Fatalf("failed to read testdata/example.json: %v", err)
	}

	var r recipes.Recipe
	// Intentionally not discarding unknown fields. We need to make sure that every field is parsed.
	um := protojson.UnmarshalOptions{DiscardUnknown: false}
	if err := um.Unmarshal(data, &r); err != nil {
		t.Fatalf("failed to unmarshal example.json into recipes.Recipe: %v", err)
	}

	if !r.HasContext() || r.GetContext() == nil {
		t.Fatalf("expected context to be present in recipe")
	}
	ctx := r.GetContext()
	entries := ctx.GetEntries()
	if len(entries) < 2 {
		t.Fatalf("expected at least 2 context entries, got %d", len(entries))
	}
	if got := entries[0].GetPath(); got != "specs/goal.md" {
		t.Errorf("first context entry path mismatch: got %q", got)
	}
	if entries[0].GetFrom() == nil || entries[0].GetFrom().GetGithub() == nil {
		t.Fatalf("expected first context entry to have github source")
	}
	if got := entries[0].GetFrom().GetGithub().GetPath(); got != "https://github.com/opensdd/recipes/global/agents_md/resources/goal.md" {
		t.Errorf("first context entry github.path mismatch: got %q", got)
	}

	if !r.HasIde() || r.GetIde() == nil || r.GetIde().GetCommands() == nil {
		t.Fatalf("expected ide.commands to be present in recipe")
	}
	cmds := r.GetIde().GetCommands().GetEntries()
	if len(cmds) != 3 {
		t.Fatalf("expected 3 commands, got %d", len(cmds))
	}
	wantNames := []string{"agents_md_plan", "agents_md", "agents_md_generate"}
	for i, c := range cmds {
		if c.GetName() != wantNames[i] {
			t.Errorf("command %d name: got %q, want %q", i, c.GetName(), wantNames[i])
		}
		if c.GetFrom() == nil || c.GetFrom().GetGithub() == nil || c.GetFrom().GetGithub().GetPath() == "" {
			t.Errorf("command %d expected github path present", i)
		}
	}
}
